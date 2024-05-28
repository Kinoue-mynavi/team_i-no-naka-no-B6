import React from "react";
import "./style.css";
import { Header } from "../../components/Header";
import { Footer } from "../../components/Footer";

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