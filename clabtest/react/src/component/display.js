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
    }, []);
  
    return (
        <div className="tab">
            <p>{data.tab}</p>
        </div>
    );
}
  
export default Display;