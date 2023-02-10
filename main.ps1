cls
Remove-NetFirewallRule -DisplayName 'Host'
try{
    Set-ExecutionPolicy Undefined
    cls

    write-host @"
     **      **                    **  
    /**     /**                   /**  
    /**     /**  ******   ****** ******
    /********** **////** **//// ///**/ 
    /**//////**/**   /**//*****   /**  
    /**     /**/**   /** /////**  /**  
    /**     /**//******  ******   //** 
    //      //  //////  //////     //  

"@

    [string]$path = Read-Host "[Server] Enter your site directory path"

    if ($path | Test-Path){
        cd $path
        try{
            [int]$port = Read-Host "[Server] Enter a port"
            if (1000 -lt $port -and $port -lt 65535){
                New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port
                New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port
                "[Server] I'm ready."
                try{
                    "[Server] http://" + (Invoke-WebRequest -uri "https://api.ipify.org/").Content + "/"
                    python -m http.server $port
                }catch{"[Server] You have no connection."}
            }else {"[Server] The port must be between 1000 and 65535."}
        }catch{"[Server] The chosen port is not valid."}
    }else{"[Server] The path you entered does not exist."}
}catch{cls
"[Server] You don't have permission for launch me."}
