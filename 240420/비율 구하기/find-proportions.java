import java.io.*;
import java.util.*;
import java.util.Map.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        TreeMap<String, Integer> tm = new TreeMap<>();

        int n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++){

            String str = br.readLine();

            if(tm.getOrDefault(str, -1) == -1){
                // 값이 없으면
                tm.put(str, 1);
            }else{
                int nxtCnt = tm.get(str) + 1;
                tm.remove(str);
                tm.put(str, nxtCnt);
            }
        }

        Iterator<Entry<String, Integer>> it = tm.entrySet().iterator();

        int sumVal = 0;

        while(it.hasNext()){
            Entry<String, Integer> entry = it.next();
            sumVal = sumVal + entry.getValue();
        }

        it = tm.entrySet().iterator();

        while(it.hasNext()){
            Entry<String, Integer> entry = it.next();
            String k = entry.getKey();
            int v = entry.getValue();
            // 반올림
            double per = (double) v * 100 / sumVal;
            per = Math.round(per*10000)/10000.0;

            // 스트링 포맷팅
            String formatted = String.format("%.4f", per);
            bw.write(k + " " + formatted + "\n");
        }

        bw.flush();
        bw.close();
    }
}