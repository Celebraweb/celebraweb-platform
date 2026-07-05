export default function Header() {
  return (
    <header
      style={{
        background: "#ffffff",
        padding: "20px 30px",
        borderBottom: "1px solid #ddd",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <div>
        <strong>CelebraWeb XOP</strong>
      </div>

      <div>Administrador</div>
    </header>
  );
}