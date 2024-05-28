import React from "react";
import "./style.css";

type Props = {
    label: string;
    children: React.ReactNode;
    isRequired?: boolean;
};

export const FormControl: React.FC<Props> = ({ label, children, isRequired = false }) => {
    return (
        <div className="container">
            <label className="label">
                {label}
                {isRequired && (
                    <span className="required-badge">*</span>
                )}
            </label>
            {children}
        </div>
    )
}