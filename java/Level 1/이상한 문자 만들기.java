class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr = s.split("");
        int cnt = 0;
        
        for (int i=0;i<arr.length;i++){
            if(arr[i].equals(" ")){ // 문자열 비교
                cnt = 0;
                answer += " ";
                continue;
            }
            if(cnt%2==0)
                answer += arr[i].toUpperCase(); // char형은 Character.toUpperCase(charvar)
            else
                answer += arr[i].toLowerCase();
            cnt += 1;
        }
        
        return answer;
    }
}