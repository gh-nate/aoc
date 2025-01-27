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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 1000

static const char *fmt = "%u,%u";

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return EXIT_FAILURE;
	}

	FILE *fp = fopen(argv[1], "r");
	if (!fp) {
		return EXIT_FAILURE;
	}

	unsigned int lights_part_1[SIZE][SIZE] = {0};
	unsigned int lights_part_2[SIZE][SIZE] = {0};

	char *t, s[] = "turn off 999,999 through 999,999\n";
	unsigned int j, x1, y1, x2, y2, lit = 0, brightness = 0;
	while (fgets(s, 34, fp)) {
		j = 0;
		if (strstr(s, "turn off")) {
			j = 9;
		} else if (strstr(s, "turn on")) {
			j = 8;
		} else if (strstr(s, "toggle")) {
			j = 7;
		}
		if (!j) {
			continue;
		}
		t = s + j;
		sscanf(t, fmt, &x1, &y1);
		t = strrchr(t, ' ') + 1;
		sscanf(t, fmt, &x2, &y2);
		switch (j) {
			case 9:
				for (; x1 <= x2; x1++) {
					for (j = y1; j <= y2; j++) {
						if (lights_part_1[j][x1]) {
							lights_part_1[j][x1] = 0;
							lit--;
						}
						if (lights_part_2[j][x1]) {
							lights_part_2[j][x1]--;
							brightness--;
						}
					}
				}
				break;
			case 8:
				for (; x1 <= x2; x1++) {
					for (j = y1; j <= y2; j++) {
						if (!lights_part_1[j][x1]) {
							lights_part_1[j][x1] = 1;
							lit++;
						}
						lights_part_2[j][x1]++;
						brightness++;
					}
				}
				break;
			case 7:
				for (; x1 <= x2; x1++) {
					for (j = y1; j <= y2; j++) {
						if (lights_part_1[j][x1]) {
							lights_part_1[j][x1] = 0;
							lit--;
						} else {
							lights_part_1[j][x1] = 1;
							lit++;
						}
						lights_part_2[j][x1] += 2;
						brightness += 2;
					}
				}
				break;
		}
	}

	if (ferror(fp)) {
		fclose(fp);
		return EXIT_FAILURE;
	}

	if (fclose(fp) == EOF) {
		return EXIT_FAILURE;
	}

	int rv = printf("Part 1: %u\n", lit);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	rv = printf("Part 2: %u\n", brightness);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
