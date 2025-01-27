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

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define STRLEN 16

bool is_nice_part_1(const char *s) {
	unsigned int vowel_count = 0;
	bool has_twins = false;
	char c, p = '\0';
	do {
		c = *s;
		if ((p == 'a' && c == 'b') ||
			(p == 'c' && c == 'd') ||
			(p == 'p' && c == 'q') ||
			(p == 'x' && c == 'y')) {
			return false;
		} else if (p == c) {
			has_twins = true;
		}
		switch (c) {
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				vowel_count++;
				break;
		}
		p = c;
	} while (*s++);
	return vowel_count >= 3 && has_twins;
}

bool is_nice_part_2(const char *s) {
	bool has_property = false;
	size_t pairs[STRLEN - 1][3];
	char c, n;
	for (size_t i, j = 0; j < STRLEN - 1 && !has_property; j++) {
		i = j + 1;
		c = s[j];
		n = s[i];
		for (size_t k = 0; k < j; k++) {
			if (pairs[k][0] != j &&
				pairs[k][1] == c &&
				pairs[k][2] == n) {
				has_property = true;
				break;
			}
		}
		pairs[j][0] = i;
		pairs[j][1] = c;
		pairs[j][2] = n;
	}
	if (!has_property) {
		return false;
	}
	has_property = false;
	for (size_t i = 0; i < STRLEN - 2; i++) {
		if (s[i] == s[i + 2]) {
			has_property = true;
			break;
		}
	}
	return has_property;
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return EXIT_FAILURE;
	}

	FILE *fp = fopen(argv[1], "r");
	if (!fp) {
		return EXIT_FAILURE;
	}

	unsigned int part_1_count = 0, part_2_count = 0;

	char s[STRLEN + 1];
	s[STRLEN] = '\0';

	while (fscanf(fp, "%s\n", s) == 1) {
		if (is_nice_part_1(s)) {
			part_1_count++;
		}
		if (is_nice_part_2(s)) {
			part_2_count++;
		}
	}

	if (ferror(fp)) {
		fclose(fp);
		return EXIT_FAILURE;
	}

	if (fclose(fp) == EOF) {
		return EXIT_FAILURE;
	}

	int rv = printf("Part 1: %u\n", part_1_count);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	rv = printf("Part 2: %u\n", part_2_count);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
