/*
 * Copyright (c) 2025 gh-nate
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include <lauxlib.h>
#include <lua.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

static const char *fmt = "%d,%d";

#define remember_position(x, y)\
	lua_pushfstring(L, fmt, x, y);\
	lua_pushboolean(L, 1);\
	lua_settable(L, 1);

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return EXIT_FAILURE;
	}

	FILE *fp = fopen(argv[1], "r");
	if (!fp) {
		return EXIT_FAILURE;
	}

	lua_State *L = luaL_newstate();
	if (!L) {
		fclose(fp);
		return EXIT_FAILURE;
	}

	lua_newtable(L);

	int x = 0, y = 0;
	remember_position(x, y);

	int c;
	while ((c = fgetc(fp)) != EOF) {
		switch (c) {
			case '^':
				y++;
				break;
			case 'v':
				y--;
				break;
			case '>':
				x++;
				break;
			case '<':
				x--;
				break;
		}
		remember_position(x, y);
	}

	if (ferror(fp)) {
		lua_close(L);
		fclose(fp);
		return EXIT_FAILURE;
	}

	lua_pushnil(L);

	unsigned int visited_houses;
	for (visited_houses = 0; lua_next(L, 1); visited_houses++) {
		lua_copy(L, -2, -1);
		lua_pushnil(L);
		lua_settable(L, 1);
	}

	int rv = printf("Part 1: %u\n", visited_houses);
	if (rv < 0) {
		lua_close(L);
		fclose(fp);
		return EXIT_FAILURE;
	}

	rewind(fp);
	x = y = 0;
	remember_position(x, y);
	int rx = x, ry = y;

	bool valid;
	unsigned int index = 0;
	while ((c = fgetc(fp)) != EOF) {
		valid = true;
		switch (c) {
			case '^':
				index % 2 ? y++ : ry++;
				break;
			case 'v':
				index % 2 ? y-- : ry--;
				break;
			case '>':
				index % 2 ? x++ : rx++;
				break;
			case '<':
				index % 2 ? x-- : rx--;
				break;
			default:
				valid = false;
				break;
		}
		if (valid) {
			remember_position(x, y);
			remember_position(rx, ry);
			index++;
		}
	}

	if (ferror(fp)) {
		lua_close(L);
		fclose(fp);
		return EXIT_FAILURE;
	}

	if (fclose(fp) == EOF) {
		lua_close(L);
		return EXIT_FAILURE;
	}

	lua_pushnil(L);

	for (visited_houses = 0; lua_next(L, 1); visited_houses++) {
		lua_pop(L, 1);
	}

	lua_close(L);

	rv = printf("Part 2: %u\n", visited_houses);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
