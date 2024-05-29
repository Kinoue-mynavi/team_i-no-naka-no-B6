import React from "react";

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement>;

type Props = {
    type?: ButtonProps["type"];
    children: React.ReactNode;
} & Omit<ButtonProps, "type">;

export const Button: React.FC<Props> = ({ children, type = "button", ...restProps }) => {
    return (
        <button {...restProps} type={type}>{children}</button>
    );
};