#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
  char info[101];
  struct Node *next;
} Node;

typedef Node *NodePtr;

NodePtr enqueue(NodePtr fila, char *info)
{
  NodePtr new = (NodePtr)malloc(sizeof(Node));
  strcpy(new->info, info);
  new->next = fila;
  return new;
}

char* dequeue(NodePtr fila)
{
  if (fila == NULL)
  {
    return NULL;
  }
  else
  {
    NodePtr node = fila;
    NodePtr prev = NULL;

    while (node->next != NULL)
    {
      prev = node;
      node = node->next;
    }

    char *info = strdup(node->info);

    if (prev != NULL)
    {
      prev->next = NULL;
    }
    else
    {
      fila = NULL;
    }
    free(node);

    return info;
  }
}

int main(){
  NodePtr fila = NULL;
  char string[101];

  string[0] = "1";

  fila = enqueue(fila, string[0]);
  fila = enqueue(fila, "2");
  fila = enqueue(fila, "3");

  printf("%s\n", dequeue(fila));
  printf("%s\n", dequeue(fila));
  printf("%s\n", dequeue(fila));

  return 0;
}