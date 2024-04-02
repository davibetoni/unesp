#include <iostream>
#include <string.h>

using namespace std;

typedef struct Node{
  int value;
  Node *left;
  Node *right;
} *Node;

void pos(Node tree, string s){
  if(tree != NULL){
    pos(tree->left, s);
    pos(tree->right, s);
    s += tree->value;
  }
}


int main()
{
  int c;
  int n;
  string pre, in;

  cin >> c;

  while (c > 0)
  {
    cin >> n >> pre >> in;

    c--;
  }

  return 0;
}
