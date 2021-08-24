import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int m;
    static int[] nums;
    static boolean[] visited;
    static List<Integer> temp = new ArrayList<>();
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        visited = new boolean[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        dfs(0);
        br.close();
        bw.close();
    }

    static void dfs(int start) throws IOException {
        if (temp.size() == m) {
            for(int j = 0; j < temp.size(); j++){
                bw.write(temp.get(j)+" ");
            }
            bw.newLine();
            bw.flush();
            return;
        }
        int remeberMe = 0;
        for(int i = start; i < n; i++){
            if (remeberMe != nums[i]){
                temp.add(nums[i]);
                remeberMe = nums[i];
                dfs(i);
                temp.remove(temp.size() - 1);
            }
        }
    }
}
