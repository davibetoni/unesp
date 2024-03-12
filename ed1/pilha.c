#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
  int info;
  struct Node *next;
} Node;

Node* push(Node *node, int x){
  Node *new = (Node*)malloc(sizeof(Node));
  new->info = x;
  new->next = node->next;
  node->next = new;

  return node;
}

int pop(Node *node){
  if(node->next == NULL){
    printf("Pilha vazia\n");
    return -1;
  }

  Node *pop = node->next;
  int info = pop->info;
  node->next = pop->next;
  free(pop);

  return info;
}

int main(){
  Node *pilha = (Node*)malloc(sizeof(Node));
  
  pilha = push(pilha, 10);
  pilha = push(pilha, 5);
  pilha = push(pilha, 2);

  printf("%d\n", pop(pilha));
  printf("%d\n", pop(pilha));
  printf("%d\n", pop(pilha));

  return 0;
}