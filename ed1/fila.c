#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
  int info;
  struct Node *next;
} Node;

Node* enqueue(Node *fila, int info){
  Node *new = (Node*)malloc(sizeof(Node));
  new->info = info;
  new->next = fila;
  return new;
}

int dequeue(Node *fila){
  if(fila == NULL){
    printf("Fila vazia\n");
    return -1;
  }

  Node *node = fila;
  Node *prev = NULL;
  while(node->next != NULL){
    prev = node;
    node = node->next;
  }

  int info = node->info;
  if(prev != NULL){
    prev->next = NULL;
  }
  free(node);

  return info;
}

int main(){
  Node *fila = NULL;

  fila = enqueue(fila, 10);
  fila = enqueue(fila, 5);
  fila = enqueue(fila, 2);

  printf("%d\n", dequeue(fila));
  printf("%d\n", dequeue(fila));
  printf("%d\n", dequeue(fila));

  return 0;
}