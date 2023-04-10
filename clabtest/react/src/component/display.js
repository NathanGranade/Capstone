// Importing modules
import React, { useState, useEffect } from "react";
  
function Display () {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        tab: "",
    });
  
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/display").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    tab: data.tab,
                });
            })
        );
    }, [])
    if (window.performance) {
        if (performance.navigation.type === 1) {
          return(
            <body>
                <div class="tab">
                    <p>{""}</p>
                    
                </div>
                </body>
          );
        } else {
            return (
                <body>
                <div class="tab">
                    <p>{data.tab}</p>
                    
                </div>
                </body>
            );
        }
      };
   
   
}
  
export default Display;