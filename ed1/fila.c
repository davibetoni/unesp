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

  Node *l = fila;
  
  while(l->next != NULL){
    if(l->next->next == NULL){
      int info = l->next->info;
      free(l->next);
      l->next = NULL;
      return info;
    }
    
    l = l->next;
  }

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