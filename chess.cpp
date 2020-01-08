#include <vector>
#include <iostream>

#define COUNT 14

using namespace std;
typedef struct {
	int x;
	int y;
} cell_t;

bool is_hitten(cell_t i, cell_t j)
{
	bool res = (i.x == j.x || i.y == j.y || abs(i.x - j.x) == abs(i.y - j.y));
	return res;
}

int is_ok_solution(vector <cell_t> v)
{
	bool is_hit = false;
	for (int i = 0; i < v.size(); i++)
		for (int j = i + 1; j < v.size(); j++)
			if (is_hitten(v[i], v[j]))
				is_hit = true;
	return !is_hit;
}
				

vector <vector <cell_t>> find(vector <cell_t> &subres,
		vector  <cell_t> &deck)
{
	if (deck.size() == 0) {
		vector <vector <cell_t>> res;
		if (subres.size() >= COUNT) {
			vector <cell_t> r;
			for (auto i : subres)
				r.push_back(i);
			res.push_back(r);
		}
		return res;
	}
	
	cell_t elem = deck[deck.size() - 1];
	deck.pop_back();
	vector <vector <cell_t>> res1 = find(subres, deck);
	deck.push_back(elem);
	
	vector <cell_t> subdeck;
	for (auto i : deck) {
		if (!is_hitten(elem, i))
			subdeck.push_back(i);
	}
	
	subres.push_back(elem);
	vector <vector <cell_t>> res2 = find(subres, subdeck);
	subres.pop_back();
	for (auto i : res2)
		res1.push_back(i);
	
	return res1;
}

int main(int argc, char **argv)
{
	vector <cell_t> deck;
	for (int i = 0; i < COUNT; i++)
		for (int j = 0; j < COUNT; j++) {
			cell_t c = {i, j};
			deck.push_back(c);
		}
	vector <cell_t> subres;
	vector <vector <cell_t>> res = find(subres, deck);
	
	for (auto i : res) {
		for (auto j :  i){
			cout << "(" << j.x << ", " << j.y << ") ";
		}
		cout << " -- " << is_ok_solution(i) << endl;
	}
	cout << res.size();
	
	return 0;
}