import React from "react";


function NavBar(props) {
    return (
        <h1 className="bg-indigo-200 text-black w-10 h-10">hello {props.name}</h1>
    )
}

export default NavBar;