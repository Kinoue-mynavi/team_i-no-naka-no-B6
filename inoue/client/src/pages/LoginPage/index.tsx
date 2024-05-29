import React from "react";
import { PageLayout } from "../../layout/PageLayout";
import { FormControl } from "../../components/modules/FormControl";
import { TextInput } from "../../components/atoms/TextInput";
import "./style.css"
import { Button } from "react-bootstrap";

const LoginPage: React.FC = () => {
    return (
        <PageLayout>
            <h2>ログインページ</h2>
            <form action="" className="form">
                <div className="inputs-container">
                    <FormControl label="ユーザ名">
                        <TextInput placeholder="ユーザ名を入力" />
                    </FormControl>
                    <FormControl label="パスワード">
                        <TextInput placeholder="パスワードを入力" />
                    </FormControl>

                    <Button type="submit">ログイン</Button>
                </div>
            </form>
        </PageLayout>
    );
};

export default LoginPage;