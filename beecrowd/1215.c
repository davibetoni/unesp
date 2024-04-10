#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct TreeNode
{
  char word[201];
  struct TreeNode *left;
  struct TreeNode *right;
} TreeNode;

typedef TreeNode *TreeNodePtr;

TreeNodePtr newNode(char *word)
{
  TreeNodePtr node = (TreeNodePtr)malloc(sizeof(TreeNode));
  strcpy(node->word, word);
  node->left = node->right = NULL;
  return node;
}

TreeNodePtr insert(TreeNodePtr node, char *word)
{
  if (node == NULL)
    return newNode(word);

  int comparison = strcasecmp(word, node->word);
  if (comparison < 0)
    node->left = insert(node->left, word);
  else if (comparison > 0)
    node->right = insert(node->right, word);

  return node;
}

void printInOrder(TreeNodePtr node)
{
  if (node != NULL)
  {
    printInOrder(node->left);
    printf("%s\n", node->word);
    printInOrder(node->right);
  }
}

void freeTree(TreeNodePtr node)
{
  if (node != NULL)
  {
    freeTree(node->left);
    freeTree(node->right);
    free(node);
  }
}

int main()
{
  TreeNodePtr root = NULL;
  char line[201], word[201];
  int j = 0;

  while (fgets(line, sizeof(line), stdin) != NULL)
  {
    for (int i = 0; i < strlen(line); i++)
    {
      if (isalpha(line[i]))
      {
        word[j++] = tolower(line[i]);
      }
      else
      {
        if (strlen(word) > 0)
        {
          root = insert(root, word);
        }

        j = 0;
        memset(word, 0, 201);
      }
    }
  }

  printInOrder(root);

  freeTree(root);

  return 0;
}