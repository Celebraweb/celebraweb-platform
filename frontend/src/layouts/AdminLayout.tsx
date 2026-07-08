import Footer from "../components/layout/Footer";
import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";

type Props = {
  children?: React.ReactNode;
};

export default function AdminLayout({
  children,
}: Props) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "260px 1fr",
        minHeight: "100vh",
        background: "#eef2f7",
      }}
    >
      <Sidebar />

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          minHeight: "100vh",
        }}
      >
        <Header />

        <main
          style={{
            flex: 1,
            padding: "32px",
            overflow: "auto",
          }}
        >
          <div
            style={{
              background: "#ffffff",
              borderRadius: "12px",
              padding: "32px",
              minHeight: "100%",
              boxShadow:
                "0 2px 8px rgba(0,0,0,0.05)",
            }}
          >
            {children}
          </div>
        </main>

        <Footer />
      </div>
    </div>
  );
}