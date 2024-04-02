#include <iostream>
#include <stack>
#include <queue>

using namespace std;

stack<int> start(stack<int> stack, int n)
{
  for (int i = n; i > 0; i--)
  {
    stack.push(i);
  }

  return stack;
}

stack<int> fuel(stack<int> discarded, stack<int> bottom)
{
  while (bottom.size() > 0)
  {
    discarded.push(bottom.top());
    bottom.pop();
  }

  return discarded;
}

int main()
{
  int n = 1;
  queue<int> inserted;

  while (n != 0)
  {
    cin >> n;
    if (n == 0)
      break;

    inserted.push(n);
  }

  while (inserted.size() > 0)
  {
    if (inserted.empty())
      break;

    int i = 0, remaining = 0;
    n = inserted.front();
    stack<int> discarded = start(discarded, n), bottom;
    queue<int> puts;

    while (i < n)
    {
      if (discarded.size() == 0)
        discarded = fuel(discarded, bottom);

      if (discarded.size() > 0)
      {
        puts.push(discarded.top());
        discarded.pop();
      }

      if (discarded.size() == 0)
        discarded = fuel(discarded, bottom);

      if (discarded.size() > 0)
      {
        bottom.push(discarded.top());
        discarded.pop();
      }

      i++;
    }

    cout << "Discarded cards: ";
    while (puts.size() > 0)
    {
      cout << puts.front();
      puts.pop();

      if (puts.size() > 1)
      {
        cout << ", ";
      }
      else
      {
        remaining = puts.front();
        puts.pop();
      }
    }

    cout << "\nRemaining card: " << remaining << endl;
    inserted.pop();
  }

  return 0;
}
