#include <stdio.h>
}


void kruskalMST(int **cost, int V) {
	int parent[V], rank[V];
	int mst_weight = 0;
	int edge_count = 0;
	int edge_number = 0;

	for(int i=0; i<V; i++){
		parent[i] = i;
		rank[i] = 0;
	}
	while(edge_count < V-1){
		int min = 9999;
		int u = -1, v = -1;
		int i;
		int j;
		for(i=0; i<V; i++){
			for(j=0; j<V; j++){
				if(cost[i][j] != 0 && FIND(parent, i) != FIND(parent,j)){
					if(cost[i][j] < min){
						min = cost[i][j];
						u=i;
						v=j;
					}
				}
			}
		}
		if(u!= -1 && v!=-1){
			UNION(parent, rank, u, v);
			printf("Edge %d:(%d, %d) cost:%d\n",edge_number,u, v, min);
			mst_weight = mst_weight + min;
			edge_count = edge_count + 1;
			edge_number++;
		}
	}
	printf("Minimum cost= %d\n",mst_weight);
}
int main() {
    int V;
    printf("No of vertices: ");
    scanf("%d", &V);

    int **cost = (int **)malloc(V * sizeof(int *));
    for (int i = 0; i < V; i++)
        cost[i] = (int *)malloc(V * sizeof(int));

    printf("Adjacency matrix:\n");
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            scanf("%d", &cost[i][j]);

    kruskalMST(cost, V);

    for (int i = 0; i < V; i++)
        free(cost[i]);
    free(cost);

    return 0;
}