#include <iostream>
#include <string.h>
#include <queue>

using namespace std;

string pos(string pre, string in)
{
  string str;
  int n = in.size();

  if(n == 0) return "";

  if(n == 1) return in;

  int root = pre.find(in[0]);

  // TODO

  return str;
}

int main()
{
  int c, n;
  queue<string> puts;
  string pre, in, str;

  cin >> c;

  for(int i = 0; i < c; i++)
  {
    cin >> n >> pre >> in;

    str = pos(pre, in);

    puts.push(str);
    str.clear();
  }

  for(int i = 0; i < c; i++)
  {
    cout << puts.front() << endl;
    puts.pop();
  }

  return 0;
}
