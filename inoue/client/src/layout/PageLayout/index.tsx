import React from "react";
import "./style.css";
import { Header } from "../../components/atoms/Header";
import { Footer } from "../../components/atoms/Footer";

type Props = {
    children: React.ReactNode;
}

export const PageLayout: React.FC<Props> = ({ children }) => {
    return (
        <div>
            <Header />
            <main className="main">
                {children}
            </main>
            <Footer />
        </div>
    );
};