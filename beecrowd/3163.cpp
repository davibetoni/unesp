#include <iostream>
#include <queue>

using namespace std;

int main()
{
  queue<string> leste;
  queue<string> norte;
  queue<string> sul;
  queue<string> oeste;

  string in = "  ";
  string puts;
  char polo;

  while (in.size() > 1)
  {
    cin >> in;

    if (in[0] == '-')
    {
      polo = in[1];
      continue;
    }

    if (polo == '4' && in.size() > 1)
    {
      leste.push(in);
    }
    else if (polo == '3' && in.size() > 1)
    {
      norte.push(in);
    }
    else if (polo == '2' && in.size() > 1)
    {
      sul.push(in);
    }
    else if (polo == '1' && in.size() > 1)
    {
      oeste.push(in);
    }
  }

  while (!leste.empty() || !norte.empty() || !sul.empty() || !oeste.empty())
  {
    if (!oeste.empty()){
      puts += oeste.front() + " ";
      oeste.pop();
    }
    
    if (!norte.empty()){
      puts += norte.front() + " ";
      norte.pop();
    }

    if (!sul.empty()){
      puts += sul.front() + " ";
      sul.pop();
    }

    if (!leste.empty()){
      puts += leste.front() + " ";
      leste.pop();
    }
  }

  puts.pop_back();

  cout << puts << endl;
  return 0;
}
