#include <iostream>
#include <string.h>
#include <queue>

using namespace std;

int main()
{
  int c, n, j = 0;
  queue<string> puts;
  string pre, in, str;

  cin >> c;

  while (j < c)
  {
    cin >> n >> pre >> in;

    for (int i = 0; i < n; i++)
    {
      
    }

    puts.push(str);
    str.clear();
    j++;
  }


  for(int i = 0; i < c; i++)
  {
    cout << puts.front() << endl;
    puts.pop();
  }

  return 0;
}
