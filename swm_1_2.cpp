#include<iostream>
using namespace std;

int main(){

  int p, n, h;
  cin >> p >> n >> h;

  int pc_num[n], pc_time[n];
  int max[p] = {0};

  for(int i = 0; i<n; i++){
    cin >> pc_num[i] >> pc_time[i];
    int p0 = pc_num[i];
    if (pc_time[i]<=h && h>=max[p0-1]+pc_time[i]){
      max[p0-1] += pc_time[i];
    }
  }

  for(int i = 0; i<p; i++){
    cout<< i+1 << max[i]*1000 << endl;
  }

  return 0;
}