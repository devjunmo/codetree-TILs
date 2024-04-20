import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        TreeMap<Integer, Integer> tm = new TreeMap<>();

        int idx = 1;
        for(int num : arr){
            // bw.write(num + "\n");
            if(!tm.containsKey(num)){
                tm.put(num, idx);
                idx++;
            }
        }

        for(Map.Entry<Integer, Integer> entry : tm.entrySet()){
            bw.write(entry.getKey() + " " + entry.getValue() + "\n");
        }

        bw.flush();
        bw.close();
    }
}