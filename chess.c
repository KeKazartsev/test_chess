#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#define COUNT 15

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

typedef struct {
	int x;
	int y;
} cell_t;

int is_ok_solution(cell_t res[COUNT]) {
	int r = 1;
	for (int i = 0; i < COUNT; i++) {
		for (int j = i + 1; j < COUNT; j++)
			r = r && (res[i].x != res[j].x) && (res[i].y != res[j].y) && (abs(res[i].x - res[j].x) != abs(res[i].y - res[j].y));
	}
	return r;
}

void add_cell(int x, int y, int deck[COUNT][COUNT], int increment)
{
	for (int i = 0; i < COUNT; i++) {
		deck[x][i] += increment;
		deck[i][y] += increment;
	}

	// main diagonal
	int d = MIN(x, y);
	for (int cx = x - d, cy = y - d; cx < COUNT && cy < COUNT; cx++, cy++) {
		assert(cx >= 0 && cx < COUNT && cy >= 0 && cy < COUNT);
		deck[cx][cy] += increment;
	}
	// side diagonal
	d = MIN(COUNT - x - 1, y);
	for (int cx = x + d, cy = y - d; cx >= 0 && cy < COUNT; cx--, cy++) {
		assert(cx >= 0 && cx < COUNT && cy >= 0 && cy < COUNT);
		deck[cx][cy] += increment;
	}
}

void put_figure(int x, int y, int deck[COUNT][COUNT]) { add_cell(x, y, deck, +1); }
void remove_figure(int x, int y, int deck[COUNT][COUNT]) { add_cell(x, y, deck, -1); }

int solution_count;		
int calls[COUNT] = {0};
int calls_sum = 0;

void find (cell_t subres[COUNT], int line, int deck[COUNT][COUNT])
{
	if (line == COUNT) {
		solution_count++;
		for (int i = 0; i < COUNT; i++)
			printf("( %d, %d ) ", subres[i].x, subres[i].y);
		int is_ok = is_ok_solution(subres);
		assert(is_ok);
		printf(" -- %d\n", is_ok);
		return;
	}
	calls[line]++;
	calls_sum++;
	
	for (int x = 0; x < COUNT; x++) {
		if (deck[x][line] != 0)
			continue;
		put_figure(x, line, deck);
		subres[line].x = x;
		subres[line].y = line;
		find(subres, line + 1, deck);
		remove_figure(x, line, deck);
	}	
}

int main()
{	
	cell_t subres[COUNT];
	int deck[COUNT][COUNT] = {0};
	find(subres, 0, deck);
	
	printf("COUNT = %d, Solutions_count == %d, calls = %d, details = ", COUNT, solution_count, calls_sum);
	for (int i = 0; i < COUNT; i++)
		printf("%d  ", calls[i]);
	printf("\n");
}
	
	