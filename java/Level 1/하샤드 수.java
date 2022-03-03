class Solution {
    public boolean solution(int x) {        
        int sum = 0;
        
        int xx = x;
        
        while(xx > 0) {
            sum += xx%10;
            xx /= 10;
        }
        
        if (x%sum == 0) {
            return true;
        } else {
            return false;
        }
    }
}