#include <stdio.h>


int binarySearch(int arr[],int low,int high,int target){
    if(low>high)
        return -1;
    int mid = low + (high-low) / 2;
    if(arr[mid] == target)
        return mid;
    else if (arr[mid] > target)
        return binarySearch(arr, low, mid-1, target);
    else
        return binarySearch(arr,mid+1,high,target);
}

void bubbleSort(int arr[], int n){
    for (int i=0; i<n-1;i++){
        for (int j=0; j<n-i-1;j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
int main(){
    int arr[] = {14,2,10,6,12,4,8};
    int n = sizeof(arr)/sizeof(arr[0]);
    int target = 10;
    bubbleSort(arr, n); //Sort the array before binary search
    int result = binarySearch(arr,0,n-1,target);
    if (result != -1)
        printf("Element found at index %d", result);
    else
        printf("Element not found");
}
