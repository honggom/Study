import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] seq = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                if(seq[i] > seq[j] && dp[i] < dp[j]){
                    dp[i] = dp[j];
                }
            }
            dp[i] += 1;
        }
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}