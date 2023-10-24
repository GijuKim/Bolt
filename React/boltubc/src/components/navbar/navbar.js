import React from 'react';
import styles from './css/navbar.css';
import logo from '../../images/logo/bolt.png';


const Navbar = () => {
    const logo_style = {
        width: '30px',
    };

    const selected_text_style = {
        color: '#E0D9FA', 
        margin: '0', 
        fontWeight: '800', 
        fontSize: '18px', 
        position: 'relative', 
        top: '11px', 
        paddingLeft: '14px',
    }

    const gap = {
        width: '20px',
    }

    const borderLine = {
        width: '20px',
        borderRight: '2px solid#E0D9FA',
        opacity: '0.5',
    }

    
    return(
        
    <div className="nav_bar">
        <div style={{display: 'flex'}}>
            <img src={logo} style={logo_style} />
            <p style={selected_text_style}>Home</p>
            <div class="nav_bar_rest">
                <div style={borderLine}></div>
                <p className="nav_bar_text">About</p>
                <div style={gap}></div>
                <p className="nav_bar_text">Events</p>
                <div style={gap}></div>
                <p className="nav_bar_text">Team</p>
            </div>
        </div>
    </div>
    );
};

export default Navbar;