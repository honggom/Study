import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        long[] cache = new long[101];
        cache[0] = 0; cache[1] = cache[2] = 1; cache[3] = 2;

        for(int i = 4; i < 101; i++){
            cache[i] = cache[i - 1] + cache[i - 2];
        }

        System.out.println(cache[n]);
        br.close();
    }
}