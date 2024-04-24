import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        for(int i=0; i<t; i++){
            TreeSet<Integer> ts = new TreeSet<>();
            int k = Integer.parseInt(br.readLine());
            for(int j = 0; j<k; j++){
                String[] cmds = br.readLine().split(" ");
                String cmd = cmds[0];
                String cmdv = cmds[1];
                
                switch(cmd){
                    case "I":
                        ts.add(Integer.parseInt(cmdv));
                        break;
                    case "D":
                        if (ts.size() != 0){
                            if(cmdv.equals("1")){
                                int mx = ts.last();
                                ts.remove(mx);
                            }else if(cmdv.equals("-1")){
                                int mn = ts.first();
                                ts.remove(mn);
                            }
                        }
                        break;
                    
                }
            }
            if(ts.size() == 0){
                bw.write("EMPTY" + "\n");
            }else{
                int mxv = ts.last();
                int mnv = ts.first();
                bw.write(Integer.toString(mxv) + " " + Integer.toString(mnv) + "\n");
            }
            
        }

        bw.flush();
        bw.close();
    }
}