class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int m = arr1.length;
        int n = arr1[0].length;
        
        int[][] answer = new int[m][n];
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                int tmp = arr1[i][j] + arr2[i][j];
                answer[i][j] = tmp;
            }
        } 
            
            
        return answer;
    }
}