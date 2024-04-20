import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        TreeMap<Integer, Integer> tm = new TreeMap<>();
        
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            String[] cmdset = br.readLine().split(" ");
            String cmd = cmdset[0];
            //System.out.println(cmd);
            if (cmd.equals("add")){
                tm.put(Integer.parseInt(cmdset[1]), Integer.parseInt(cmdset[2]));
                
            }else if(cmd.equals("remove")){
                tm.remove(Integer.parseInt(cmdset[1]));

            }else if(cmd.equals("find")){
                int res = tm.getOrDefault(Integer.parseInt(cmdset[1]), -1);
                if(res == -1){
                    bw.write("None" + "\n");
                }else{
                    //System.out.println(res);
                    bw.write(Integer.toString(res) + "\n");
                }
            }

        }
        
        bw.flush();
        bw.close();
        

    }
}