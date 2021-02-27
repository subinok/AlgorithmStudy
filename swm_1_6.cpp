#include<iostream>
#include<algorithm>
using namespace std;
int findmax(int* arr, int n);

int main(){
  int n;
  cin >> n;
  int arr[n];

  for(int i = 0; i<n; i++){
    cin >> arr[i];
  }  

  cout << findmax(arr, n) << endl;

  return 0;
}

int findmax(int* arr, int n){
  int max = -1, max_pos = -1;

  if(n == 2){
    if(arr[0] > arr[1]) return arr[0];
    else return arr[1];
  }
  else{
    for(int i = 0; i<n; i++){
      if(arr[i]>max){
        max = arr[i];
        max_pos = i;
      }
    }
  if (max_pos>=n/2) return max + findmax(arr, n/2);
  else return max + findmax(arr+n/2, n/2);
  }
}