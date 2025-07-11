int linearSearch(int arr[],int size,int target,int index){
     if (index >= size){
          return -1;
     }
     if (arr[index] == target){
          return index;
     }
     return linearSearch(arr,size,target,index+1);
}

int main(){
     int arr[] = {2,4,6,8,10};
     int size = sizeof(arr)/sizeof(arr[0]);
     int target = 6;
     int result = linearSearch(arr,size,target,0);
     if(result == -1){
        printf("Element %d is not found here.", target);
     }
     else{
        printf("Element %d is found at %d index.",target, result);
     }
     return 0;
}
