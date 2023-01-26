cls
set-ExecutionPolicy Unrestricted
python -m pip install -r requirements.txt
python -m pip install --upgrade pip
Remove-NetFirewallRule -DisplayName 'Host'
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

if ($path | Test-Path){
    cd $path
    try{
        [int]$port = Read-Host "[Server] Enter a port"
        if (1000 -lt $port -and $port -lt 65535){
            New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port
            New-NetFirewallRule -DisplayName 'Host' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $port
            "[Server] I'm ready."
            "[Server] " + (Invoke-WebRequest -uri "https://api.ipify.org/").Content
            python -m http.server $port
        }else {
            "[Server] The port must be between 1000 and 65535."}
    }catch{
    "[Server] The chosen port is not valid."}
}else{
    "[Server] The path you entered does not exist."
}
