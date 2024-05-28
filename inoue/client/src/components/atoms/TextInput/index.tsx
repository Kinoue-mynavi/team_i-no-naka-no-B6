import React from "react";
import "./style.css";

type Props = React.InputHTMLAttributes<HTMLInputElement>;

export const TextInput: React.FC<Props> = (props) => {
    return <input {...props} type="text" className="input" />;
}