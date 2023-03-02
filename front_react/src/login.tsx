import { useAuth0 } from "@auth0/auth0-react";

export default function LoginButton () {
  const { loginWithRedirect, isAuthenticated, logout } = useAuth0();

  return !isAuthenticated ? (
      <button onClick={() => loginWithRedirect()}>ログイン</button>
  ) : (
      <button onClick={() => logout()}>ログアウト</button>
  )
};

