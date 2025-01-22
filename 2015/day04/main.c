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

#include <limits.h>
#include <nettle/md5.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ATTEMPTS 10000000
#if MAX_ATTEMPTS > UINT_MAX
#error "integer overflow"
#endif

#define NUMBER_OF_OCTETS 3

static const char *fmt = "%u";

unsigned int mine(const char *input, unsigned int number_of_zeroes) {
	char data[16] = {0};
	strncpy(data, input, 8);

	const size_t sz = strlen(data);

	uint8_t digest[NUMBER_OF_OCTETS];
	struct md5_ctx md5_ctx;
	md5_init(&md5_ctx);

	for (unsigned int n = 0; n < MAX_ATTEMPTS; n++) {
		if (sprintf(data + sz, fmt, n) < 0) {
			break;
		}
		md5_update(&md5_ctx, strlen(data), data);
		md5_digest(&md5_ctx, NUMBER_OF_OCTETS, digest);
		switch (number_of_zeroes) {
			case 5:
				if (!digest[0] && !digest[1] && !(digest[2] >> 4)) {
					return n;
				}
				break;
			case 6:
				if (!digest[0] && !digest[1] && !digest[2]) {
					return n;
				}
				break;
			default:
				n = MAX_ATTEMPTS;
				break;
		}
	}
	return 0;
}

int main(void) {
	const char *input = getenv("input");
	if (!input) {
		return EXIT_FAILURE;
	}

	unsigned int n = mine(input, 5);
	if (!n) {
		return EXIT_FAILURE;
	}

	int rv = printf("Part 1: %u\n", n);
	if (rv < 0) {
		return EXIT_FAILURE;
	}

	n = mine(input, 6);
	if (!n) {
		return EXIT_FAILURE;
	}

	rv = printf("Part 2: %u\n", n);
	if (rv < 0) {
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
