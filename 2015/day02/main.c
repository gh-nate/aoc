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

unsigned int wrapping_paper(const unsigned int l, const unsigned int w, const unsigned int h) {
	const unsigned int area_lw = l*w, area_wh = w*h, area_hl = h*l;
	unsigned int smallest_side = area_lw > area_wh ? area_wh : area_lw;
	if (smallest_side > area_hl) {
		smallest_side = area_hl;
	}
	const unsigned int surface_area = 2*area_lw + 2*area_wh + 2*area_hl;
	return surface_area + smallest_side;
}

unsigned int ribbon(const unsigned int l, const unsigned int w, const unsigned int h) {
	const unsigned int perimeter_lw = 2*l + 2*w, perimeter_wh = 2*w + 2*h, perimeter_hl = 2*h + 2*l;
	unsigned int smallest_perimeter = perimeter_lw > perimeter_wh ? perimeter_wh : perimeter_lw;
	if (smallest_perimeter > perimeter_hl) {
		smallest_perimeter = perimeter_hl;
	}
	const unsigned int volume = l*w*h;
	return smallest_perimeter + volume;
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return EXIT_FAILURE;
	}

	FILE *fp = fopen(argv[1], "r");
	if (!fp) {
		return EXIT_FAILURE;
	}

	int rv;
	unsigned int l, w, h, total_wrapping_paper = 0, total_ribbon = 0;
	while ((rv = fscanf(fp, "%ux%ux%u\n", &l, &w, &h)) == 3) {
		total_wrapping_paper += wrapping_paper(l, w, h);
		total_ribbon += ribbon(l, w, h);
	}

	if (fclose(fp) == EOF) {
		return EXIT_FAILURE;
	}

	rv = printf("Part 1: %u\n", total_wrapping_paper);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	rv = printf("Part 2: %u\n", total_ribbon);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
