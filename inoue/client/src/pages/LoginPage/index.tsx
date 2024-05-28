import React from "react";
import { PageLayout } from "../../layout/PageLayout";
import { Link } from "react-router-dom";

const LoginPage: React.FC = () => {
    return (
        <PageLayout>
            <h1>Login Page</h1>
            <Link to="/">ホームに戻る</Link>
        </PageLayout>
    );
};

export default LoginPage;