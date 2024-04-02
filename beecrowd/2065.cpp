#include <iostream>
#include <queue>

using namespace std;

int main()
{
  int workers, customers;
  int time[10005], itens[10005];
  queue<int> working;
  int total = 0;
  int w = 0, c = 0;

  cin >> workers >> customers;

  for (int i = 0; i < workers; i++)
  {
    cin >> time[i];
  }

  for (int j = 0; j < customers; j++)
  {
    cin >> itens[j];
  }

  while(c < customers)
  {
    for (int j = w; j < workers; j++)
    {
      if (j > c)
      {
        w = j;
        break;
      }

      working.push(itens[c] * time[j]);
      c++;
    }

    int maior = 0;
    while(!working.empty())
    { 
      int atual = working.front();
      
      if(atual > maior)
        maior = atual;

      total += maior;

      working.pop();
    }
  }
  cout << total << endl;

  return 0;
}