import Footer from "../components/layout/Footer";
import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";

type Props = {
  children?: React.ReactNode;
};

export default function AdminLayout({ children }: Props) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "260px 1fr",
        minHeight: "100vh",
      }}
    >
      <Sidebar />

      <div
        style={{
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Header />

        <main
          style={{
            flex: 1,
            padding: "40px",
            background: "#f4f6f8",
          }}
        >
          {children}
        </main>

        <Footer />
      </div>
    </div>
  );
}