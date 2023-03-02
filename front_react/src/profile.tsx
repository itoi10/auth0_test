import { useAuth0 } from "@auth0/auth0-react";

export default function Profile() {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    isAuthenticated ? (
      <>
        <dl>
          <dt>名前</dt>
          <dd>{user?.name}</dd>
          <dt>メールアドレス</dt>
          <dd>{user?.email}</dd>
        </dl>
      </>
    ) : <></>
  )
}
