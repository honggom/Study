import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.Math;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> dp = new ArrayList<>();
        dp.add(nums[0]);

        for(int i = 0; i < n -1; i++){
            dp.add(Math.max(dp.get(i) + nums[i + 1], nums[i + 1]));
        }
        System.out.println(Collections.max(dp));
    }
}