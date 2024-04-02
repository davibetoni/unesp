#include <stdio.h>
#include <stdlib.h>

typedef struct node_tree
{
  int value;
  struct node_tree *left;
  struct node_tree *right;
} *def_tree;

void insert(def_tree *tree, int value)
{
  def_tree branch;

  if ((*tree) != NULL)
  {
    if ((*tree)->value > value)
    {
      insert(&((*tree)->left), value);
    }
    else if ((*tree)->value < value)
    {
      insert(&((*tree)->right), value);
    }
    else
    {
      printf("Valor já existe na árvore\n");
    }
  }
  else
  {
    branch = (def_tree)malloc(sizeof(def_tree));
    branch->value = value;
    branch->left = NULL;
    branch->right = NULL;
    *tree = branch;
  }
}

void print_in_order(def_tree tree)
{
  if (tree != NULL)
  {
    print_in_order(tree->left);
    printf("%d", tree->value);
    print_in_order(tree->right);
  }
}

int find(def_tree tree, int value)
{
  if (tree == NULL)
  {
    return 0;
  }

  return tree->value == value || find(tree->left, value) || find(tree->right, value);
}

int main()
{
  def_tree tree = NULL;

  insert(&tree, 10);
  insert(&tree, 5);
  insert(&tree, 2);
  insert(&tree, 7);

  print_in_order(tree);
  return 0;
}