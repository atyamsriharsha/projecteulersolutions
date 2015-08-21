var N,a,b,n1,n2,m1,m2:Int64;
begin
     read(N);
     read(a);
     read(b);
     if a=3 then
        begin
            n1:=1;
            n2:=1;
            m1:=1;
            m2:=1;
        while (m1<N) and (m2<N) do
        begin
            if m1=m2 then
            begin
                WriteLn(m1);
                n1:=n1+1;
                n2:=n2+1;
                m1:=n1*(n1+1) div 2 ;
                m2:=n2*(3*n2-1) div 2;
            end
            else if (m1<m2) then
            begin
                n1:=n1+1;
                m1:=n1*(n1+1) div 2 ;
            end
            else
            begin
                n2:=n2+1 ;
                m2:=n2*(3*n2-1) div 2 ;
            end
        end;
     end
     else
        begin
            n1:=1;
            n2:=1;
            m1:=1;
            m2:=1;
            while (m1<N) and (m2<N) do
                begin
                    if m1=m2 then
                    begin
                        WriteLn(m1);
                        n1:=n1+1;
                        n2:=n2+1;
                        m1:=n1*(2*n1-1)  ;
                        m2:=n2*(3*n2-1) div 2;
                    end
                    else if (m1<m2) then
                    begin
                        n1:=n1+1;
                        m1:=n1*(2*n1-1) ;
                    end
                    else
                    begin
                        n2:=n2+1 ;
                        m2:=n2*(3*n2-1) div 2 ;
                    end;
                end;
        end;
end.