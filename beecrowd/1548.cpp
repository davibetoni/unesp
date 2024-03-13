#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

queue<int> order(queue<int> q){
  queue<int> ordered;
  int size = q.size();
  int grades[size];
  int i = 0;

  while(!q.empty()){
    grades[i] = q.front();
    q.pop();
    i++;
  }

  for(int i = 0; i < size; i++){
    for(int j = i; j < size; j++){
      if(grades[i] < grades[j]){
        int aux = grades[i];
        grades[i] = grades[j];
        grades[j] = aux;
      }
    }
  }

  for(int i = 0; i < size; i++){
    ordered.push(grades[i]);
  }

  return ordered;
}

int compare(queue<int> q1, queue<int> q2){
  int size = q1.size();
  int count = 0;

  for(int i = 0; i < size; i++){
    if(q1.front() == q2.front()){
      count++;
    }
    q1.pop();
    q2.pop();
  }

  return count;
}

int main()
{
  int n;
  queue<int> not_switches;
  cin >> n;

  for(int i = 0; i < n; i++)
  {
    int students;
    queue<int> queue;

    cin >> students;

    for(int j = 0; j < students; j++)
    {
      int grade;
      cin >> grade;
      queue.push(grade);
    }

    not_switches.push(compare(queue, order(queue)));
  }

  while(!not_switches.empty()){
    cout << not_switches.front() << endl;
    not_switches.pop();
  }

  return 0;
}